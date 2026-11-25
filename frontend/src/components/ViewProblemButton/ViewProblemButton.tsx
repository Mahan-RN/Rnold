import { Link } from "react-router";
import styles from "src/components/ViewProblemButton/ViewProblemButton.module.css";

import type { CurriculumProblemResponse } from "../../loaders/HomePageLoader";

interface ViewProblemButtonProps extends CurriculumProblemResponse {
    problemIndex: number;
    accepted: boolean;
}

export default function ViewProblemButton(props: ViewProblemButtonProps) {
    const id = props.id;
    const title = props.title;
    const difficulty = props.difficulty;
    const index = props.problemIndex;
    const accepted = props.accepted;

    let difficultyElm;
    if (difficulty === 1) {
        difficultyElm = <span className={styles.easy}>Easy</span>;
    } else if (difficulty === 2) {
        difficultyElm = <span className={styles.normal}>Medium</span>;
    } else {
        difficultyElm = <span className={styles.hard}>Hard</span>;
    }

    return (
        <Link
            to={`problems/${id}`}
            state={{ position: index }}
            className={styles.problemLink}
        >
            <span className={styles.problemTitle}>{title}</span>
            <span className={styles.completion}>
                {accepted && "Completed ✅"}
            </span>
            {difficultyElm}
        </Link>
    );
}
