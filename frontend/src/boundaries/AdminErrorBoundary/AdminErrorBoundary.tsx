import { isRouteErrorResponse, useRouteError } from "react-router";
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
                    <img className={styles.requestDenied} src={requestDenied} />
                </div>
            );
        }

        return (
            <div>
                <h1>
                    Error {error.status}: {error.statusText}
                </h1>
                <img className={styles.requestDenied} src={requestDenied} />
            </div>
        );
    }
    return <h1>Something went wrong</h1>;
}
