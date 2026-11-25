import { isRouteErrorResponse, Link, useRouteError } from "react-router";
import notFound from "src/assets/notFound.gif";
import styles from "src/boundaries/RootErrorBoundary/RootErrorBoundary.module.css";

export default function RootErrorBoundary() {
    const error = useRouteError();

    if (isRouteErrorResponse(error)) {
        return (
            <div role="alert">
                <h1>
                    {error.status} {error.statusText}
                </h1>
                <p>{error.data || "Something went wrong with this request."}</p>
                <Link to="/">Go back home</Link>
                <img className={styles.errorImg} src={notFound} />
            </div>
        );
    }

    if (error instanceof Error) {
        return (
            <div role="alert">
                <h1>Application Error</h1>
                <p>{error.message}</p>
                {import.meta.env.DEV && <pre>{error.stack}</pre>}
                <Link to="/">Go back home</Link>
                <img className={styles.errorImg} src={notFound} />
            </div>
        );
    }

    return (
        <div role="alert">
            <h1>Unknown Error</h1>
            <Link to="/">Go back home</Link>
        </div>
    );
}
