import { useLoaderData, useParams } from "react-router";
import type problemPageLoader from "src/loaders/ProblemPageLoader";
import Markdown from "react-markdown";
import styles from "src/pages/ProblemPage/ProblemPage.module.css";
import CodeEditor from "src/components/CodeEditor/CodeEditor";

export default function Path() {
    const params = useParams();
    const problemID = params.problemID;
    const loaderData = useLoaderData<typeof problemPageLoader>();
    const problem = loaderData.problem;
    const difficulty = problem.difficulty;

    let difficultyElm;
    if (difficulty === 1) {
        difficultyElm = <span className={styles.easy}>Easy</span>;
    } else if (difficulty === 2) {
        difficultyElm = <span className={styles.normal}>Medium</span>;
    } else {
        difficultyElm = <span className={styles.hard}>Hard</span>;
    }

    return (
        <div className={styles.flexContainer}>
            <div className={styles.titleContainer}>
                <h1>
                    Problem {problemID}: {problem.title}
                </h1>
                <h3>{difficultyElm}</h3>
            </div>
            <h2>Description:</h2>
            <Markdown>{problem.description}</Markdown>
            <CodeEditor starterCode={problem.starter_code} />
        </div>
    );
}
