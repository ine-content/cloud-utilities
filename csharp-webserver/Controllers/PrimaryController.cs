using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using System.Net;

namespace csharp_webserver.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class PrimaryController : ControllerBase
    {
        [HttpGet("echo")]
        public ActionResult<string> Echo()
        {
            string hostName = Dns.GetHostName();
            Console.WriteLine(hostName);

            // Get the IP from GetHostByName method of dns class.
            string IP = Dns.GetHostEntry(hostName).AddressList[0].ToString();
            return new OkObjectResult(new HostData
            {
                hostName = Request.Host.ToString(),
                hostIp = IP,
                computerName = Environment.MachineName,
                remoteIp = HttpContext.Connection != null ? HttpContext.Connection.RemoteIpAddress.ToString() : ""
            }); ;
        }
    }

    public class HostData
    {
        public string? hostName { get; set; }
        public string? hostIp { get; set; }
        public string? computerName { get; set; }
        public string? remoteIp { get; set; }
    }
}
