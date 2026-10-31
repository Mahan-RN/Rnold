import CodeMirror from "@uiw/react-codemirror";
import { materialDark } from "@uiw/codemirror-theme-material";

interface CodeEditorProps {
    starterCode: string;
}

export default function CodeEditor({ starterCode }: CodeEditorProps) {
    return (
        <CodeMirror value={starterCode} height="200px" theme={materialDark}/>
    )
}