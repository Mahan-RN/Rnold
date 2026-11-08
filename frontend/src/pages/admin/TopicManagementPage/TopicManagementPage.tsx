import { useActionData, useLoaderData } from "react-router";
import type topicAction from "src/actions/admin/topicAction";
import CreateTopicForm from "src/components/admin/CreateTopicForm/CreateTopicForm";
import TopicCollapsible from "src/components/admin/TopicCollapsible/TopicCollapsible";
import type topicManagementPageLoader from "src/loaders/admin/TopicManagementPageLoader";
import styles from "src/pages/admin/TopicManagementPage/TopicManagementPage.module.css";

export default function TopicManagementPage() {
    const topics = useLoaderData<typeof topicManagementPageLoader>();
    const actionData = useActionData<typeof topicAction>();

    let actionAlertElement;
    if (!actionData) {
        actionAlertElement = <></>;
    } else if (actionData.success) {
        actionAlertElement = (
            <p className={styles.SuccessMessage}>{actionData.message}</p>
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
            <div className={styles.topicForm}>
                {actionAlertElement}
                <CreateTopicForm />
            </div>
            <hr />
            <div className={styles.collapsibleContainer}>
                {topics.map((topic) => (
                    <TopicCollapsible {...topic} />
                ))}
            </div>
        </div>
    );
}
