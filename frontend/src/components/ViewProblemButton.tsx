import type { CurriculumProblemResponse } from "../loaders/HomePageLoader";

export default function ViewProblemButton(props: CurriculumProblemResponse) {
    // const id = props.id // TODO
    const title = props.title
    const difficulty = props.difficulty
    return (
        <button>
            <span>{title}</span>
            <span>{difficulty}</span>
        </button>
    )
}