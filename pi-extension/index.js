export default function standInExtension(pi) {
  const sendInterview = (args, ctx) => {
    const tail = String(args || "").trim();
    const message = tail ? `/skill:stand-in ${tail}` : "/skill:stand-in";

    if (ctx?.isIdle?.() === false) {
      pi.sendUserMessage(message, { deliverAs: "followUp" });
      ctx?.ui?.notify?.("stand-in queued as follow-up.", "info");
      return;
    }

    pi.sendUserMessage(message);
  };

  pi.registerCommand("stand-in", {
    description: "Interview evidence-backed stand-ins for your target users",
    handler: sendInterview
  });
}
