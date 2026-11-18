import { useLocation, useLoaderData } from "react-router";
import type problemPageLoader from "src/loaders/ProblemPageLoader";
import Markdown from "react-markdown";
import styles from "src/pages/ProblemPage/ProblemPage.module.css";
import CodeEditor from "src/components/CodeEditor/CodeEditor";
import TestCasePanel from "src/components/TestCasePanel/TestCasePanel";
import { useState } from "react";
import type { TestResult } from "src/services/rubSubmission";

export default function ProblemPage() {
    const loaderData = useLoaderData<typeof problemPageLoader>();
    const problem = loaderData.problem;
    const testCases = loaderData.testCases;
    const difficulty = problem.difficulty;

    const location = useLocation();
    const position = location.state?.position;

    const [testResults, setTestResults] = useState<TestResult[] | null>(null);

    let difficultyElm;
    if (difficulty === 1) {
        difficultyElm = <span className={styles.easy}>Easy</span>;
    } else if (difficulty === 2) {
        difficultyElm = <span className={styles.normal}>Medium</span>;
    } else {
        difficultyElm = <span className={styles.hard}>Hard</span>;
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
                <h3>{difficultyElm}</h3>
            </div>
            <div className={styles.descriptionContainer}>
                <h2>Description:</h2>
                <Markdown>{problem.description}</Markdown>
            </div>
            <CodeEditor
                starterCode={problem.starter_code}
                testCases={testCases}
                onTestResults={setTestResults}
            />
            {testCaseElements}
        </div>
    );
}
