import { StreamLanguage } from "@codemirror/language";
import { r } from "@codemirror/legacy-modes/mode/r";
import { materialDark } from "@uiw/codemirror-theme-material";
import CodeMirror from "@uiw/react-codemirror";
import { useState } from "react";
import { useFetcher, useRouteLoaderData } from "react-router";
import styles from "src/components/CodeEditor/CodeEditor.module.css";
import OutputTerminal from "src/components/OutputTerminal/OutputTerminal";
import type { TestCasesResponse } from "src/loaders/ProblemPageLoader";
import type rootLayoutLoader from "src/loaders/RootLayoutLoader";
import type { TestResult } from "src/services/rubSubmission";
import { runSubmission } from "src/services/rubSubmission";

interface CodeEditorProps {
    problemID: number;
    starterCode: string;
    testCases: TestCasesResponse[];
    onTestResults: (results: TestResult[] | null) => void;
}

const extensions = [StreamLanguage.define(r)];

export default function CodeEditor({
    problemID,
    starterCode,
    testCases,
    onTestResults,
}: CodeEditorProps) {
    const user = useRouteLoaderData<typeof rootLayoutLoader>("root");

    const [code, setCode] = useState(starterCode);
    const [output, setOutput] = useState("");
    const [isRunning, setIsRunning] = useState(false);

    const fetcher = useFetcher();

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

            let num_test_cases_passed = 0;
            if (result.testResults && user?.github_id) {
                for (const testCase of result.testResults) {
                    if (testCase.passed) {
                        num_test_cases_passed += 1;
                    }
                }
                let accepted = false;
                if (num_test_cases_passed === testCases.length) {
                    accepted = true;
                }
                fetcher.submit(
                    {
                        accepted: accepted,
                        problemID: problemID,
                    },
                    {
                        method: "post",
                        encType: "application/json",
                    },
                );
            }
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
