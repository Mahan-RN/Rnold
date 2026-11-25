
import { useState } from "react";
import Markdown from "react-markdown";
import { useLoaderData, useLocation } from "react-router";
import CodeEditor from "src/components/CodeEditor/CodeEditor";
import TestCasePanel from "src/components/TestCasePanel/TestCasePanel";
import type problemPageLoader from "src/loaders/ProblemPageLoader";
import styles from "src/pages/ProblemPage/ProblemPage.module.css";
import type { TestResult } from "src/services/rubSubmission";

export default function ProblemPage() {
    const loaderData = useLoaderData<typeof problemPageLoader>();
    const problem = loaderData.problem;
    const testCases = loaderData.testCases;
    const accepted = loaderData.accepted;
    const difficulty = problem.difficulty;

    const location = useLocation();
    const position = location.state?.position;

    const [testResults, setTestResults] = useState<TestResult[] | null>(null);

    let difficultyElm;
    if (difficulty === 1) {
        difficultyElm = (
            <span className={`${styles.badge} ${styles.easy}`}>
                Easy
            </span>
        );
    } else if (difficulty === 2) {
        difficultyElm = (
            <span className={`${styles.badge} ${styles.normal}`}>
                Medium
            </span>
        );
    } else {
        difficultyElm = (
            <span className={`${styles.badge} ${styles.hard}`}>
                Hard
            </span>
        );
    }

    const testCaseElements = testCases.map((testCase, index) => (
        <TestCasePanel
            key={testCase.id}
            testCase={testCase}
            num={index + 1}
            result={testResults?.[index]}
        />
    ));

    return (
        <div className={styles.flexContainer}>
            <div className={styles.titleContainer}>
                <h1>
                    Problem #{position}: {problem.title}
                </h1>

                <div className={styles.infoContainer}>
                    {difficultyElm}

                    {accepted !== null && (
                        <span
                            className={`${styles.status} ${
                                accepted
                                    ? styles.completed
                                    : styles.incomplete
                            }`}
                        >
                            <span aria-hidden="true">
                                {accepted ? "✓" : "✕"}
                            </span>
                            {accepted ? "Completed" : "Incomplete"}
                        </span>
                    )}
                </div>
            </div>

            <div className={styles.descriptionContainer}>
                <h2>Description:</h2>
                <Markdown>{problem.description}</Markdown>
            </div>

            <CodeEditor
                problemID={problem.id}
                starterCode={problem.starter_code}
                testCases={testCases}
                onTestResults={setTestResults}
            />

            <div className={styles.testCasesContainer}>
                {testCaseElements}
            </div>
        </div>
    );
}
