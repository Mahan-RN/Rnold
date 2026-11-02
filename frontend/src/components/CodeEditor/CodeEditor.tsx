import CodeMirror from "@uiw/react-codemirror";
import { materialDark } from "@uiw/codemirror-theme-material";
import styles from "src/components/CodeEditor/CodeEditor.module.css";
import { StreamLanguage } from "@codemirror/language";
import { r } from "@codemirror/legacy-modes/mode/r";
import { useState } from "react";
import OutputTerminal from "src/components/OutputTerminal/OutputTerminal";
import { runSubmission } from "src/services/rubSubmission";
import type { TestResult } from "src/services/rubSubmission";
import type { TestCasesResponse } from "src/loaders/ProblemPageLoader";

interface CodeEditorProps {
    starterCode: string;
    testCases: TestCasesResponse[];
    onTestResults: (results: TestResult[] | null) => void;
}

const extensions = [StreamLanguage.define(r)];

export default function CodeEditor({
    starterCode,
    testCases,
    onTestResults,
}: CodeEditorProps) {
    const [code, setCode] = useState(starterCode);
    const [output, setOutput] = useState("");
    const [isRunning, setIsRunning] = useState(false);

    async function handleClickSubmit() {
        setIsRunning(true);
        setOutput("");
        onTestResults(null);
        try {
            const result = await runSubmission(
                code,
                testCases.map((t) => t.code),
            );
            setOutput(result.output);
            onTestResults(result.testResults);
        } catch (err) {
            setOutput(String(err));
        } finally {
            setIsRunning(false);
        }
    }

    function handleClickReset() {
        setCode(starterCode);
        setOutput("");
        onTestResults(null);
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
