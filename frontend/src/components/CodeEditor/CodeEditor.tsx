import CodeMirror from "@uiw/react-codemirror";
import { materialDark } from "@uiw/codemirror-theme-material";
import styles from "src/components/CodeEditor/CodeEditor.module.css";
import { StreamLanguage } from "@codemirror/language";
import { r } from "@codemirror/legacy-modes/mode/r";
import { useState } from "react";
import getWebR from "src/services/webr";
import OutputTerminal from "src/components/OutputTerminal/OutputTerminal";
import { WebRError, Shelter } from "webr";
import type { REnvironment } from "webr";

interface CodeEditorProps {
    starterCode: string;
}

interface RawOutputEntry {
    type: string;
    data: unknown;
}

const extensions = [StreamLanguage.define(r)];

export default function CodeEditor({ starterCode }: CodeEditorProps) {
    const [code, setCode] = useState(starterCode);
    const [output, setOutput] = useState("");
    const [isRunning, setIsRunning] = useState(false);

    function parseOutput(output: RawOutputEntry[]) {
        const text = output
            .filter((e) => e.type === "stdout" || e.type === "stderr")
            .map((e) => String(e.data))
            .join("\n");

        return text === "" ? "Code Successfully Submitted ✨" : text;
    }

    async function handleClickSubmit() {
        setIsRunning(true);
        setOutput("");
        let shelter: Shelter | undefined;
        try {
            const webR = await getWebR();
            shelter = await new webR.Shelter();
            const env = (await shelter.evalR(
                "new.env(parent = globalenv())",
            )) as REnvironment;
            const result = await shelter.captureR(code, {
                env: env,
                withAutoprint: true,
                captureConditions: false,
            });
            setOutput(parseOutput(result.output));
        } catch (err) {
            setOutput(err instanceof WebRError ? err.message : String(err));
        } finally {
            await shelter?.purge();
            setIsRunning(false);
        }
    }

    function handleClickReset() {
        setCode(starterCode);
        setOutput("");
    }

    return (
        <div className={styles.codeEditor}>
            <div className={styles.controlBar}>
                <p>R Code</p>
                <div>
                    <button
                        type="button"
                        onClick={handleClickSubmit}
                        disabled={isRunning}
                    >
                        {isRunning ? "Running ..." : "Submit"}
                    </button>
                    <button
                        type="button"
                        onClick={handleClickReset}
                        disabled={isRunning}
                    >
                        Reset
                    </button>
                </div>
            </div>
            <CodeMirror
                value={code}
                extensions={extensions}
                onChange={(value) => setCode(value)}
                minHeight="200px"
                maxHeight="500px"
                theme={materialDark}
                basicSetup={{ autocompletion: false }}
            />
            {output !== "" && <OutputTerminal output={output} />}
        </div>
    );
}
