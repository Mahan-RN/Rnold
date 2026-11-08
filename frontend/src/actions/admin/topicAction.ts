import type { ActionFunctionArgs } from "react-router";
import apiFetch from "src/api/Fetch";

export default async function topicAction({ request }: ActionFunctionArgs) {
    const formData = await request.formData();
    const intent = formData.get("intent");
    let fetchURL;
    let fetchOptions;
    let successMsg;
    if (intent === "create") {
        fetchURL = "/topics";
        const data = {
            name: formData.get("name"),
            description: formData.get("description"),
            sort_order: formData.get("sort_order"),
        };
        fetchOptions = {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
        };
        successMsg = "Topic created successfully";
    } else if (intent === "delete") {
        const topic_id = formData.get("id");
        fetchURL = `/topics/${topic_id}`;
        fetchOptions = {
            method: "DELETE",
        };
        successMsg = "Topic deleted successfully";
    } else {
        throw new Error(
            "Intent value did not match any of the supported values",
        );
    }
    try {
        await apiFetch<string | undefined>(fetchURL, fetchOptions);
        return {
            success: true,
            message: successMsg,
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
