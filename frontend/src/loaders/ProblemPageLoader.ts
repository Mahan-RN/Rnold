import type { LoaderFunctionArgs } from "react-router";
import apiFetch from "src/api/Fetch";

export interface ProblemResponse {
    title: string;
    description: string;
    difficulty: number;
    starter_code: string;
}

export default async function problemPageLoader({
    request,
    params,
}: LoaderFunctionArgs) {
    const signal = request.signal;
    const problemID = params.problemID;
    const problem = await apiFetch<ProblemResponse>(`/problems/${problemID}`, {
        signal,
    });
    return problem;
}
