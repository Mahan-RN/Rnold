import type { CurriculumProblemResponse } from "../../loaders/HomePageLoader";
import { Link } from "react-router";
import styles from "src/components/ViewProblemButton/ViewProblemButton.module.css";

interface ViewProblemButtonProps extends CurriculumProblemResponse {
    problemIndex: number;
}

export default function ViewProblemButton(props: ViewProblemButtonProps) {
    const id = props.id;
    const title = props.title;
    const difficulty = props.difficulty;
    const index = props.problemIndex;

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
            state={{ position: index}}
            className={styles.problemLink}
        >
            <span className={styles.problemTitle}>{title}</span>
            {difficultyElm}
        </Link>
    );
}
