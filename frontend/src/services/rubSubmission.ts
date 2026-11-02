import { WebRError } from "webr";
import type { REnvironment } from "webr";
import getWebR from "src/services/webr";

interface RawOutputEntry {
    type: string;
    data: unknown;
}

export interface TestResult {
    passed: boolean;
    message?: string;
}

export interface SubmissionResult {
    output: string;
    testResults: TestResult[] | null; // null means the user's code failed, so tests were skipped
}

function parseOutput(output: RawOutputEntry[]) {
    const text = output
        .filter((e) => e.type === "stdout" || e.type === "stderr")
        .map((e) => String(e.data))
        .join("\n");
    return text === "" ? "Code Successfully Submitted ✨" : text;
}

function errorText(err: unknown) {
    return err instanceof WebRError ? err.message : String(err);
}

export async function runSubmission(
    code: string,
    testCodes: string[],
): Promise<SubmissionResult> {
    const webR = await getWebR();
    const shelter = await new webR.Shelter();
    try {
        const env = (await shelter.evalR(
            "new.env(parent = globalenv())",
        )) as REnvironment;

        let output: string;
        try {
            const result = await shelter.captureR(code, {
                env: env,
                withAutoprint: true,
            });
            output = parseOutput(result.output);
        } catch (err) {
            return { output: errorText(err), testResults: null };
        }

        const testResults: TestResult[] = [];
        for (const testCode of testCodes) {
            try {
                await shelter.captureR(testCode, { env: env });
                testResults.push({ passed: true });
            } catch (err) {
                testResults.push({ passed: false, message: errorText(err) });
            }
        }
        return { output, testResults };
    } finally {
        await shelter.purge();
    }
}
