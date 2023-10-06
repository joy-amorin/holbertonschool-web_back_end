export default function guardrail(mathFunction) {
  const queue = [];
  let result = '';
  try {
    result = mathFunction();
  } catch (err) {
    queue.push(String(err));
  }

  if (result) queue.push(result);
  queue.push('Guardrail was processed');
  return queue;
}
