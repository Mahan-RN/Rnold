import type { CurriculumResponse } from "../../loaders/HomePageLoader";
import ViewProblemButton from "../ViewProblemButton/ViewProblemButton";

export default function TopicBox(props: CurriculumResponse) {
    // const topicID = props.id;
    const topicName = props.name;
    const topicDescription = props.description;
    const problems = props.problems;
    const viewProblemButtons = problems.map((problem) => (
        <li>
            <ViewProblemButton
                id={problem.id}
                title={problem.title}
                difficulty={problem.difficulty}
            />
        </li>
    ));
    return (
        <>
            <h2>{topicName}</h2>
            <p>{topicDescription}</p>
            {viewProblemButtons.length === 0 ? (
                <p>0 Problems</p>
            ) : (
                <ol>{viewProblemButtons}</ol>
            )}
        </>
    );
}
