import { useLoaderData } from "react-router";
import type homePageLoader from "src/loaders/HomePageLoader";
import TopicBox from "src/components/TopicBox/TopicBox";

export default function HomePage() {
    const curriculum = useLoaderData<typeof homePageLoader>();
    const topicBoxes = curriculum.map((topic) => (
        <TopicBox
            key={topic.id}
            id={topic.id}
            name={topic.name}
            description={topic.description}
            problems={topic.problems}
        />
    ));
    return topicBoxes.length === 0 ? <h1>0 Topics</h1> : <>{topicBoxes}</>;
}
