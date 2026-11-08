import type { ActionFunctionArgs } from "react-router";
import apiFetch from "src/api/Fetch";

export default async function createTopicAction({
    request,
}: ActionFunctionArgs) {
    const formData = await request.formData();
    const data = {
        name: formData.get("name"),
        description: formData.get("description"),
        sort_order: formData.get("sort_order"),
    };

    try {
        await apiFetch<string | undefined>(`/topics`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
        });
        return {
            success: true,
            message: `Topic created successfully`,
        };
    } catch (error) {
        if (error instanceof Response) {
            const message = await error.text();
            return {
                success: false,
                message: message,
            };
        }

        throw error;
    }
}
