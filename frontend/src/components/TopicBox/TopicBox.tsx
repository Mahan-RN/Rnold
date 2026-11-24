import styles from "src/components/TopicBox/TopicBox.module.css";
import ViewProblemButton from "src/components/ViewProblemButton/ViewProblemButton";
import type { CurriculumProblemResponse } from "src/loaders/HomePageLoader";

interface TopicBoxProps {
    topicName: string;
    topicDescription: string;
    problems: CurriculumProblemResponse[];
    completedProblems: number[] | null;
}

export default function TopicBox({
    topicName,
    topicDescription,
    problems,
    completedProblems,
}: TopicBoxProps) {
    const viewProblemButtons = problems.map((problem, index) => (
        <li>
            <ViewProblemButton
                key={problem.id}
                id={problem.id}
                title={problem.title}
                difficulty={problem.difficulty}
                problemIndex={index + 1}
                accepted={completedProblems?.includes(problem.id) ?? false}
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
