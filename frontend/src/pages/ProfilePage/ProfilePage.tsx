import { Form, useLoaderData } from "react-router";
import profilePageLoader from "src/loaders/ProfilePageLoader";
import styles from "src/pages/ProfilePage/ProfilePage.module.css";

export default function ProfilePage() {
    const loaderData = useLoaderData<typeof profilePageLoader>();

    const roleString = loaderData.role === 1 ? "User" : "Admin";

    return (
        <main className={styles.profilePage}>
            <div className={styles.profileCard}>
                <header className={styles.profileHeader}>
                    <div className={styles.avatar}>
                        {loaderData.username.charAt(0).toUpperCase()}
                    </div>

                    <div className={styles.profileHeading}>
                        <h1>{loaderData.username}</h1>
                        <span className={styles.roleBadge}>{roleString}</span>
                    </div>
                </header>

                <section className={styles.profileSection}>
                    <h2>Account Information</h2>

                    <div className={styles.infoList}>
                        <div className={styles.infoRow}>
                            <span className={styles.infoLabel}>Username</span>
                            <span className={styles.infoValue}>
                                {loaderData.username}
                            </span>
                        </div>

                        <div className={styles.infoRow}>
                            <span className={styles.infoLabel}>GitHub ID</span>
                            <span className={styles.infoValue}>
                                {loaderData.github_id}
                            </span>
                        </div>

                        <div className={styles.infoRow}>
                            <span className={styles.infoLabel}>
                                GitHub Email
                            </span>
                            <span className={styles.infoValue}>
                                {loaderData.github_email ?? "Not provided"}
                            </span>
                        </div>

                        <div className={styles.infoRow}>
                            <span className={styles.infoLabel}>
                                Account Role
                            </span>
                            <span className={styles.infoValue}>
                                {roleString}
                            </span>
                        </div>
                    </div>
                </section>

                <section className={styles.profileSection}>
                    <h2>Account Activity</h2>

                    <div className={styles.infoList}>
                        <div className={styles.infoRow}>
                            <span className={styles.infoLabel}>
                                Account Created
                            </span>
                            <span className={styles.infoValue}>
                                {loaderData.created_at}
                            </span>
                        </div>

                        <div className={styles.infoRow}>
                            <span className={styles.infoLabel}>Last Login</span>
                            <span className={styles.infoValue}>
                                {loaderData.last_login}
                            </span>
                        </div>
                    </div>
                </section>
                <section>
                    <Form method="delete" action="/delete-me">
                        <button
                            className={styles.deleteMeBtn}
                            type="submit"
                            onClick={(event) => {
                                if (
                                    !confirm(
                                        "Are you sure you want to delete your account?",
                                    )
                                ) {
                                    event.preventDefault();
                                }
                            }}
                        >
                            Delete Account
                        </button>
                    </Form>
                </section>
            </div>
        </main>
    );
}
