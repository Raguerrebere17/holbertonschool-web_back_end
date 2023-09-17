export default function taskBlock(trueOrFalse) {
	const task = false;
	const task 2 = true;

	if (trueOrFalse) {
		/* eslint-disable */
		const task = true;
		const task2 = false;
	}

	return [task, task2];
}
