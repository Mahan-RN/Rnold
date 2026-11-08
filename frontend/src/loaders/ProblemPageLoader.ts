import type { LoaderFunctionArgs } from "react-router";
import apiFetch from "src/api/Fetch";

export interface ProblemResponse {
    title: string;
    description: string;
    difficulty: number;
    starter_code: string;
}

export interface TestCasesResponse {
    id: number;
    problem_id: number;
    sort_order: number;
    code: string;
}

export default async function problemPageLoader({
    request,
    params,
}: LoaderFunctionArgs) {
    const signal = request.signal;
    const problemID = params.problemID;
    const [problem, testCases] = await Promise.all([
        apiFetch<ProblemResponse>(`/problems/${problemID}`, {
            signal,
        }),
        apiFetch<TestCasesResponse[]>(`/problems/${problemID}/test-cases`, {
            signal,
        }),
    ]);
    return { problem, testCases };
}
