import { useParams } from "react-router";

export default function Path() {
    const params = useParams();
    const problemID = params.problemID;
    return <h1>Problem {problemID}</h1>;
}
