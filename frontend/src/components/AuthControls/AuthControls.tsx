import { Form, useRouteLoaderData } from "react-router";
import type rootLayoutLoader from "src/loaders/RootLayoutLoader";
import styles from "src/components/AuthControls/AuthControls.module.css";

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
