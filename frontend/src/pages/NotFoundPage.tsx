import { Link } from "react-router";

export default function NotFoundPage() {
    return (
        <>
            <h1>404 Not Found</h1>
            <Link to="/">Home page</Link>
        </>
    );
}
