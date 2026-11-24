import { useLoaderData } from "react-router";
import TopicBox from "src/components/TopicBox/TopicBox";
import type homePageLoader from "src/loaders/HomePageLoader";
import styles from "src/pages/HomePage/HomePage.module.css";

export default function HomePage() {
    const loaderData = useLoaderData<typeof homePageLoader>();
    const curriculum = loaderData.curriculum;
    const completedProblems = loaderData.completedProblems;
    const topicBoxes = curriculum.map((topic) => (
        <TopicBox
            key={topic.id}
            topicName={topic.name}
            topicDescription={topic.description}
            problems={topic.problems}
            completedProblems={completedProblems}
        />
    ));
    return (
        <div className={styles.root}>
            {topicBoxes.length === 0 ? <h1>0 Topics</h1> : topicBoxes}
        </div>
    );
}
