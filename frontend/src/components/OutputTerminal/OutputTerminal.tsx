import { CodeBlock } from "react-code-block";
import styles from "src/components/OutputTerminal/OutputTerminal.module.css";

interface OutputTerminalProps {
    output: string;
}

export default function OutputTerminal({ output }: OutputTerminalProps) {
    return (
        <div className={styles.container}>
            <CodeBlock code={output} language="bash">
                <CodeBlock.Code className="bg-gray-900 p-6 rounded-xl shadow-lg">
                    <CodeBlock.LineContent>
                        <CodeBlock.Token />
                    </CodeBlock.LineContent>
                </CodeBlock.Code>
            </CodeBlock>
        </div>
    );
}
