import type { CurriculumResponse } from "src/loaders/HomePageLoader";
import ViewProblemButton from "src/components/ViewProblemButton/ViewProblemButton";
import styles from "src/components/TopicBox/TopicBox.module.css";

export default function TopicBox(props: CurriculumResponse) {
    // const topicID = props.id;
    const topicName = props.name;
    const topicDescription = props.description;
    const problems = props.problems;
    const viewProblemButtons = problems.map((problem, index) => (
        <li>
            <ViewProblemButton
                key={problem.id}
                id={problem.id}
                title={problem.title}
                difficulty={problem.difficulty}
                problemIndex={index + 1}
            />
        </li>
    ));
    return (
        <div className={styles.flexContainer}>
            <h2>{topicName}</h2>
            <p>{topicDescription}</p>
            {viewProblemButtons.length === 0 ? (
                <p>0 Problems</p>
            ) : (
                <ol>{viewProblemButtons}</ol>
            )}
        </div>
    );
}
