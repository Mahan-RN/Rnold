import { isRouteErrorResponse, Link, useRouteError } from "react-router";
import requestDenied from "src/assets/requestDenied.gif";
import styles from "src/boundaries/AdminErrorBoundary/AdminErrorBoundary.module.css";

export default function AdminErrorBoundary() {
    const error = useRouteError();

    if (isRouteErrorResponse(error)) {
        if (error.status === 403) {
            return (
                <div>
                    <h1>Access Denied</h1>
                    <p>{error.data}</p>
                    <Link to="/">Go back home</Link>
                    <img
                        className={styles.requestDeniedImg}
                        src={requestDenied}
                    />
                </div>
            );
        }

        return (
            <div>
                <h1>
                    Error {error.status}: {error.statusText}
                </h1>
                <Link to="/">Go back home</Link>
                <img className={styles.requestDeniedImg} src={requestDenied} />
            </div>
        );
    }
    return <h1>Something went wrong</h1>;
}
