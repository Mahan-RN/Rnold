import CodeMirror from "@uiw/react-codemirror";
import { materialDark } from "@uiw/codemirror-theme-material";
import styles from "src/components/CodeEditor/CodeEditor.module.css";
import { StreamLanguage } from "@codemirror/language";
import { r } from "@codemirror/legacy-modes/mode/r";
import { useState } from "react";
import getWebR from "src/services/webr";
import OutputTerminal from "src/components/OutputTerminal/OutputTerminal";
import { WebRError } from "webr";

interface CodeEditorProps {
    starterCode: string;
}

interface RawOutputEntry {
    type: string;
    data: unknown;
}

export default function CodeEditor({ starterCode }: CodeEditorProps) {
    const extensions = [StreamLanguage.define(r)];
    const [code, setCode] = useState(starterCode);
    const [output, setOutput] = useState("");

    function parseOutput(output: RawOutputEntry[]) {
        let finalOutput = "";
        if (output.length === 0) {
            finalOutput = "Code Successfully Submitted ✨";
        }
        for (const entry of output) {
            switch (entry.type) {
                case "stdout":
                case "stderr":
                    finalOutput += entry.data + "\n";
                    break;

                case "error":
                    finalOutput +=
                        "WebR returned an error of type RObject" + "\n";
                    // entry.data is RObject
                    break;
            }
        }
        return finalOutput;
    }

    async function handleClickSubmit() {
        const webR = await getWebR();
        try {
            const result = await webR.globalShelter.captureR(code, {
                withAutoprint: true,
            });
            setOutput(parseOutput(result.output));
        } catch (err) {
            if (err instanceof WebRError) {
                setOutput(err.message);
            }
        }
    }

    function handleClickReset() {
        setCode(starterCode);
    }

    return (
        <div className={styles.codeEditor}>
            <button type="submit" onClick={handleClickSubmit}>
                Submit
            </button>
            <button type="submit" onClick={handleClickReset}>
                Reset
            </button>
            <CodeMirror
                value={code}
                extensions={extensions}
                onChange={(value) => setCode(value)}
                minHeight="200px"
                maxHeight="500px"
                theme={materialDark}
            />
            <OutputTerminal output={output} />
        </div>
    );
}
