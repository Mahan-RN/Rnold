import { useLoaderData, useParams } from "react-router";
import type problemPageLoader from "src/loaders/ProblemPageLoader";

export default function Path() {
    const params = useParams();
    const problemID = params.problemID;
    const problem = useLoaderData<typeof problemPageLoader>();
    return (
        <>
            <h1>Problem {problemID}</h1>
            <h2>Description:</h2>
            <p>{problem.description}</p>
        </>
    );
}
