import CreateTopicForm from "src/components/admin/CreateTopicForm/CreateTopicForm";
import styles from "src/pages/admin/TopicManagementPage/TopicManagementPage.module.css";

export default function TopicManagementPage() {
    return (
        <div className={styles.flexContainer}>
            <h1>Topic Management</h1>
            <h2>Add Topic</h2>
            <CreateTopicForm />
        </div>
    );
}
