import { Collapsible } from "@base-ui/react/collapsible";
import styles from "src/components/admin/UserCollapsible/UserCollapsible.module.css";
import { Form } from "react-router";

interface UserCollapsibleProps {
    github_id: number;
    github_email: string;
    username: string;
    created_at: string;
    last_login: string;
    role: number;
}

export default function UserCollapsible({
    github_id,
    github_email,
    username,
    created_at,
    last_login,
    role,
}: UserCollapsibleProps) {
    function confirmSubmit(event: React.SubmitEvent<HTMLFormElement>) {
        const isConfirmed = window.confirm(`Delete ${username}?`);
        if (!isConfirmed) {
            event.preventDefault();
        }
    }
    return (
        <Collapsible.Root className={styles.Collapsible}>
            <Collapsible.Trigger className={styles.Trigger}>
                {username} ({github_email}) {role === 1 ? "👤" : "👑"}
                <CaretRightIcon className={styles.Icon} />
            </Collapsible.Trigger>
            <Collapsible.Panel className={styles.Panel}>
                <div className={styles.Content}>
                    <p>
                        <strong>GitHub ID:</strong> {github_id}
                    </p>
                    <p>
                        <strong>Role:</strong>{" "}
                        {role === 1 ? "User 👤" : "Admin 👑"}
                    </p>
                    <p>
                        <strong>Created At:</strong> {created_at}
                    </p>
                    <p>
                        <strong>Last Login:</strong> {last_login}
                    </p>
                    <div className={styles.Actions}>
                        <Form
                            action="/admin/users"
                            method="DELETE"
                            onSubmit={confirmSubmit}
                        >
                            <input
                                type="hidden"
                                name="github_id"
                                value={github_id}
                            />
                            <button
                                type="submit"
                                className={styles.DeleteButton}
                            >
                                Delete User
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
