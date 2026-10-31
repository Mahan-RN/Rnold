import CodeMirror from "@uiw/react-codemirror";
import { materialDark } from "@uiw/codemirror-theme-material";
import styles from "src/components/CodeEditor/CodeEditor.module.css";
import { StreamLanguage } from "@codemirror/language";
import { r } from "@codemirror/legacy-modes/mode/r";

interface CodeEditorProps {
    starterCode: string;
}

export default function CodeEditor({ starterCode }: CodeEditorProps) {
    const extensions = [StreamLanguage.define(r)];

    return (
        <div className={styles.codeEditor}>
            <CodeMirror
                value={starterCode}
                extensions={extensions}
                minHeight="200px"
                maxHeight="500px"
                theme={materialDark}
            />
        </div>
    );
}
