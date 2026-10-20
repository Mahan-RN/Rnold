import { useLoaderData } from "react-router";
import type homePageLoader from "../loaders/HomePageLoader";
import TopicBox from "../components/TopicBox";

export default function HomePage() {
    const curriculum = useLoaderData<typeof homePageLoader>();
    const topicBoxes = curriculum.map((topic) => (
        <TopicBox
            id={topic.id}
            name={topic.name}
            description={topic.description}
            problems={topic.problems}
        />
    ));
    return topicBoxes;
}
