import axios from "axios";
import type { LoaderFunctionArgs } from "react-router";

export interface CurriculumProblemResponse {
    id: number;
    title: string;
    difficulty: number;
}
export interface CurriculumResponse {
    id: number;
    name: string;
    description: string;
    problems: CurriculumProblemResponse[];
}

export default async function homePageLoader({ request }: LoaderFunctionArgs) {
    const signal = request.signal;
    const [curriculumResponse, completedProblemsResponse] = await Promise.all([
        axios.get<CurriculumResponse[]>("/api/curriculum", {
            signal,
        }),
        axios
            .get<number[]>("/api/submissions/accepted", {
                signal,
            })
            .catch((error: unknown) => {
                if (
                    axios.isAxiosError(error) &&
                    error.response?.status === 401
                ) {
                    return null;
                }
                console.log("Some other error was thrown in the homePageLoader")
                throw error;
            }),
    ]);
    console.log("Hello!")
    console.log(curriculumResponse.data)
    return {
        curriculum: curriculumResponse.data,
        completedProblems: completedProblemsResponse?.data ?? null,
    };
}
