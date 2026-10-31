import CodeMirror from "@uiw/react-codemirror";
import { materialDark } from "@uiw/codemirror-theme-material";
import styles from "src/components/CodeEditor/CodeEditor.module.css";
import { StreamLanguage } from "@codemirror/language";
import { r } from "@codemirror/legacy-modes/mode/r";
import { useState } from "react";

interface CodeEditorProps {
    starterCode: string;
}

export default function CodeEditor({ starterCode }: CodeEditorProps) {
    const extensions = [StreamLanguage.define(r)];
    const [code, setCode] = useState(starterCode);

    function handleClickSubmit() {
        console.log("User clicked submit!");
        console.log(code);
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
        </div>
    );
}
