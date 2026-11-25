import axios from "axios";
import type { LoaderFunctionArgs } from "react-router";

export interface ProblemResponse {
    id: number;
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
    const [problemResponse, testCasesResponse, submissionStatusResponse] =
        await Promise.all([
            axios.get<ProblemResponse>(`/api/problems/${problemID}`, {
                signal,
            }),
            axios.get<TestCasesResponse[]>(
                `/api/problems/${problemID}/test-cases`,
                {
                    signal,
                },
            ),
            axios
                .get<boolean>(`/api/submissions/${problemID}/me`, { signal })
                .catch((error: unknown) => {
                    if (
                        axios.isAxiosError(error) &&
                        error.response?.status === 401
                    ) {
                        return null;
                    }
                    throw error;
                }),
        ]);
    return {
        problem: problemResponse.data,
        testCases: testCasesResponse.data,
        accepted: submissionStatusResponse?.data ?? null,
    };
}
