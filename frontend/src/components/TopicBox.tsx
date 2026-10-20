import type { CurriculumResponse } from "../loaders/HomePageLoader";

export default function TopicBox(props: CurriculumResponse) {
    const topicID = props.id;
    const topicName = props.name;
    const topidDescription = props.description;
    const problems = props.problems;
    // TODO
    return (
        <>
            <h2>{topicName}</h2>
            <p>{topidDescription}</p>
            // TODO
        </>
    );
}
