import type { TestCasesResponse } from "src/loaders/ProblemPageLoader";
import { StreamLanguage } from "@codemirror/language";
import { r } from "@codemirror/legacy-modes/mode/r";
import CodeMirror from "@uiw/react-codemirror";
import { materialDark } from "@uiw/codemirror-theme-material";
import styles from "src/components/TestCasePanel/TestCasePanel.module.css";
interface TestCasePanelProps {
    testCase: TestCasesResponse;
    num: number;
}

const extensions = [StreamLanguage.define(r)];

export default function TestCasePanel({ testCase, num }: TestCasePanelProps) {
    const code = testCase.code;

    return (
        <div className={styles.panelContainer}>
            <p>Case {num}</p>
            <CodeMirror
                value={code}
                extensions={extensions}
                minHeight="50px"
                maxHeight="300px"
                theme={materialDark}
                readOnly={true}
            />
        </div>
    );
}
