import { Form, useRouteLoaderData } from "react-router";
import type rootLayoutLoader from "src/loaders/RootLayoutLoader";
import styles from "src/components/AuthControls/AuthControls.module.css";

const ADMIN_ROLE = 2;

export default function AuthControls() {
    const user = useRouteLoaderData<typeof rootLayoutLoader>("root");

    if (!user) {
        return (
            <a className={styles.loginLink} href="/api/auth/github/login">
                Log in with GitHub
            </a>
        );
    } else {
        return (
            <>
                {user.role === ADMIN_ROLE && (
                    <a href="/admin">Admin Dashboard</a>
                )}
                <span className={styles.usernameText}>{user.username}</span>
                <Form method="post" action="/logout">
                    <button className={styles.logoutBtn} type="submit">
                        Log out
                    </button>
                </Form>
            </>
        );
    }
}
