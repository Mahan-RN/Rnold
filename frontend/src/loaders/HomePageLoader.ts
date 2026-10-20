import type { LoaderFunctionArgs } from "react-router";
import apiFetch from "../api/Fetch";

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
    const curriculum = await apiFetch<CurriculumResponse[]>("/curriculum", {
        signal,
    });
    return curriculum;
}
