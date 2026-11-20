import { useLoaderData } from "react-router";
import TopicBox from "src/components/TopicBox/TopicBox";
import type homePageLoader from "src/loaders/HomePageLoader";
import styles from "src/pages/HomePage/HomePage.module.css"

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
    return (
        <div className={styles.root}>
            {topicBoxes.length === 0 ? <h1>0 Topics</h1> : topicBoxes}
        </div>
    );
}
