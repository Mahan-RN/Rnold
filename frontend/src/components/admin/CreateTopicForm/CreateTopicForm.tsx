import { Form } from "react-router";
import styles from "src/components/admin/CreateTopicForm/CreateTopicForm.module.css";

export default function CreateTopicForm() {
    return (
        <Form method="post" className={styles.form}>
            <div className={styles.header}>
                <h2>Create a topic</h2>
                <p>Add a new topic.</p>
            </div>

            <div className={styles.field}>
                <label htmlFor="topic-name">Topic Name</label>
                <input
                    id="topic-name"
                    name="name"
                    type="text"
                    placeholder="e.g. Vectors"
                    required
                />
            </div>

            <div className={styles.field}>
                <label htmlFor="description">Description</label>
                <textarea
                    id="description"
                    name="description"
                    rows={5}
                    placeholder="Describe what this topic covers..."
                    autoComplete="off"
                    required
                    minLength={50}
                    maxLength={200}
                />
                <span className={styles.hint}>
                    Between 50 and 200 characters.
                </span>
            </div>

            <div className={styles.field}>
                <label htmlFor="sort-order">Sort Order</label>
                <input
                    id="sort-order"
                    name="sort_order"
                    type="number"
                    min={0}
                    max={200}
                    step={10}
                    defaultValue={10}
                    required
                />
                <span className={styles.hint}>Must be a multiple of 10.</span>
            </div>

            <div className={styles.actions}>
                <button name="intent" value="create" type="submit">
                    <span>+</span>
                    Create Topic
                </button>
            </div>
        </Form>
    );
}
