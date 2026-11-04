import { Collapsible } from "@base-ui/react/collapsible";
import apiFetch from "src/api/Fetch";
import styles from "src/components/admin/UserCollapsible/UserCollapsible.module.css";

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
    async function handleDelete() {
        const isConfirmed = window.confirm(
            `Are you sure you want to delete user ${username}?`,
        );
        if (isConfirmed) {
            await apiFetch("/users/me", { method: "DELETE" });
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
                        <button
                            className={styles.DeleteButton}
                            onClick={handleDelete}
                        >
                            Delete User
                        </button>
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
