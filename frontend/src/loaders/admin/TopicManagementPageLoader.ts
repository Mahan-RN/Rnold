import type { LoaderFunctionArgs } from "react-router";
import apiFetch from "src/api/Fetch";

export interface TopicResponse {
    id: number,
    name: string;
    description: string;
    sort_order: number;
}

export default async function topicManagementPageLoader({
    request,
}: LoaderFunctionArgs) {
    const signal = request.signal;
    const topics = await apiFetch<TopicResponse[]>("/topics", { signal });
    return topics;
}
