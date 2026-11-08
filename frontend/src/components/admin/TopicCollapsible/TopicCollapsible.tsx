import { Collapsible } from "@base-ui/react/collapsible";
import styles from "src/components/admin/UserCollapsible/UserCollapsible.module.css";
import { Form } from "react-router";

interface TopicCollapsibleProps {
    id: number;
    name: string;
    description: string;
    sort_order: number;
}

export default function TopicCollapsible({
    id,
    name,
    description,
    sort_order,
}: TopicCollapsibleProps) {
    function confirmSubmit(event: React.SubmitEvent<HTMLFormElement>) {
        const isConfirmed = window.confirm(`Delete topic ${name}?`);
        if (!isConfirmed) {
            event.preventDefault();
        }
    }
    return (
        <Collapsible.Root className={styles.Collapsible}>
            <Collapsible.Trigger className={styles.Trigger}>
                {name}
                <CaretRightIcon className={styles.Icon} />
            </Collapsible.Trigger>
            <Collapsible.Panel className={styles.Panel}>
                <div className={styles.Content}>
                    <p>
                        <strong>ID:</strong> {id}
                    </p>
                    <p>
                        <strong>Name:</strong> {name}
                    </p>
                    <p>
                        <strong>Description:</strong> {description}
                    </p>
                    <p>
                        <strong>Sort Order:</strong> {sort_order}
                    </p>
                    <div className={styles.Actions}>
                        <Form
                            action="/admin/topics"
                            method="DELETE"
                            onSubmit={confirmSubmit}
                        >
                            <input type="hidden" name="id" value={id} />
                            <button
                                name="intent"
                                value="delete"
                                type="submit"
                                className={styles.DeleteButton}
                            >
                                Delete Topic
                            </button>
                        </Form>
                    </div>
                </div>
            </Collapsible.Panel>
        </Collapsible.Root>
    );
}

export function CaretRightIcon(props: React.ComponentProps<"svg">) {
    return (
        <svg
            width="16"
            height="16"
            viewBox="0 0 16 16"
            fill="currentColor"
            {...props}
            style={{ display: "block", ...props.style }}
        >
            {" "}
            <path d="M6 12V4l4.5 4z" />{" "}
        </svg>
    );
}
