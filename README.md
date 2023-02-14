<p>This is a Pyrogram bot that can kick members from groups and channels after a given time. The kick time can be configured through a bot command, and the default kick time is 30 days. The bot is also designed to only allow group admins to execute its commands, and it includes a whitelist feature so that certain members can be exempted from being kicked.</p>

<h2>Setup</h2>

<ol>
  <li>Clone this repository:<br>
    <code>git clone https://github.com/yourusername/yourrepository.git</code></li>

  <li>Install the required Python packages:<br>
    <code>pip install -r requirements.txt</code></li>

  <li>Set the following environment variables with your Telegram bot API key and MongoDB connection string:<br>
    <code>export BOT_TOKEN="your_bot_token_here"</code><br>
    <code>export MONGO_URL="your_mongodb_url_here"</code></li>
</ol>

<h2>Usage</h2>

<ol>
  <li>Start the bot by running:<br>
    <code>python bot.py</code></li>

  <li>Add the bot to a group or channel as an administrator.</li>

  <li>Use the <code>/settime</code> command in a private chat with the bot to set the kick time. For example:<br>
    <code>/settime 86400</code><br>
    This would set the kick time to 86400 seconds (1 day).</li>

  <li>Use the <code>/addtowhitelist</code> command in a private chat with the bot to add a member to the whitelist. For example:<br>
    <code>/addtowhitelist 123456789</code><br>
    This would add the member with user ID 123456789 to the whitelist.</li>

  <li>Wait for new members to join the group or channel. After the specified kick time has elapsed, the bot will automatically kick the members who have not been whitelisted.</li>
</ol>

<h2>License</h2>

<p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>
