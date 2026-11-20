import { StreamLanguage } from "@codemirror/language";
import { r } from "@codemirror/legacy-modes/mode/r";
import { materialDark } from "@uiw/codemirror-theme-material";
import CodeMirror from "@uiw/react-codemirror";
import styles from "src/components/TestCasePanel/TestCasePanel.module.css";
import type { TestCasesResponse } from "src/loaders/ProblemPageLoader";
import type { TestResult } from "src/services/rubSubmission";

interface TestCasePanelProps {
    testCase: TestCasesResponse;
    num: number;
    result?: TestResult;
}

const extensions = [StreamLanguage.define(r)];

export default function TestCasePanel({
    testCase,
    num,
    result,
}: TestCasePanelProps) {
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
            {result &&
                (result.passed ? <p>" ✅ Passed"</p> : <p>" ❌ Failed"</p>)}
            {result && !result.passed && <pre>{result.message}</pre>}
        </div>
    );
}
