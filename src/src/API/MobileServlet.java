package src.API;


import java.io.IOException;


import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;


import org.apache.solr.client.solrj.SolrClient;
import org.apache.solr.client.solrj.SolrQuery;
import org.apache.solr.client.solrj.SolrServerException;
import org.apache.solr.client.solrj.impl.HttpSolrClient;
import org.apache.solr.client.solrj.response.QueryResponse;
import org.apache.solr.common.SolrDocumentList;


/**
 * Servlet implementation class MobileServlet
 */
@WebServlet("/MobileServlet")
public class MobileServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public MobileServlet() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
		
	   String querytext=request.getParameter("searchtext");
	   SolrClient client =new HttpSolrClient.Builder("http://localhost:8983/solr/films").build();
	   SolrQuery query = new SolrQuery();
	   query.setQuery(querytext);
	   query.setFields("id","directed_by","initial_release_date","genre");
	   query.setStart(0);
       query.set("defType", "edismax");
       
        
       
	try {
		
		QueryResponse responseSolr = client.query(query);
		SolrDocumentList results = responseSolr.getResults();
		
		
 		for (int i = 0; i < results.size(); ++i) 
		{
		     //System.out.println(results.get(i));
		    
		}
			
			

	} 
	catch (SolrServerException e) 
	{
						// TODO Auto-generated catch block
							e.printStackTrace();
	}
       
       
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		doGet(request, response);
	}

}
