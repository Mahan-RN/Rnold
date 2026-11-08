import { useActionData, useLoaderData } from "react-router";
import type createTopicAction from "src/actions/admin/createTopicAction";
import CreateTopicForm from "src/components/admin/CreateTopicForm/CreateTopicForm";
import TopicCollapsible from "src/components/admin/TopicCollapsible/TopicCollapsible";
import type topicManagementPageLoader from "src/loaders/admin/TopicManagementPageLoader";
import styles from "src/pages/admin/TopicManagementPage/TopicManagementPage.module.css";

export default function TopicManagementPage() {
    const topics = useLoaderData<typeof topicManagementPageLoader>();
    const actionData = useActionData<typeof createTopicAction>();

    let actionAlertElement;
    if (!actionData) {
        actionAlertElement = <></>;
    } else if (actionData.success) {
        actionAlertElement = (
            <p className={styles.SuccessMessage}>Topic created successfully</p>
        );
    } else {
        actionAlertElement = (
            <p className={styles.ErrorMessage}>Error: {actionData.message}</p>
        );
    }

    return (
        <div className={styles.flexContainer}>
            <h1>Topic Management</h1>
            <h2>Add Topic</h2>
            {actionAlertElement}
            <CreateTopicForm />
            <div>
                {topics.map((topic) => (
                    <TopicCollapsible {...topic} />
                ))}
            </div>
        </div>
    );
}
